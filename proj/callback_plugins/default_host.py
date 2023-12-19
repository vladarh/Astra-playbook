
# -*- coding: utf-8 -*-
# (c) 2012-2014, Michael DeHaan <michael.dehaan@gmail.com>
# (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
    callback: default
    type: stdout
    short_description: default Ansible screen output
    version_added: historical
    description:
        - This is the default output callback for ansible-playbook.
    extends_documentation_fragment:
      - default_callback
    requirements:
      - set as stdout in configuration
'''

import os
import time
import json
from collections import MutableMapping
from os.path import expanduser
import codecs
from ansible.module_utils._text import to_bytes

from ansible import constants as C

from ansible.playbook.task_include import TaskInclude
from ansible.plugins.callback import CallbackBase
from ansible.utils.color import colorize, hostcolor


from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.executor.playbook_executor import PlaybookExecutor
#from ansible.plugins.callback import CallbackBase,call_json #,log_plays

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
temp_path = BASE_DIR + "/all_info/localhost/logs/log_localhost.log"

class CallbackModule(CallbackBase):
    
    '''
    This is the default callback interface, which simply prints messages
    to stdout when new callback events are received.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'default_host'

    def __init__(self):

        self._play = None
        self._last_task_banner = None
        super(CallbackModule, self).__init__()

    def record_msg_per_host(self, msg, delegated_vars, nl = True):

        # Статический путь

        # host = result._result.get('_ansible_delegated_vars', None)['ansible_host']
        # home_path = expanduser('~')
        # relative_playbook_dir = "/Desktop/proj/all_info"
        # full_path = home_path + relative_playbook_dir
        # custom_path = full_path + "/" + delegated_vars + "/" + "logs"

        custom_path = BASE_DIR + "/all_info" + "/" + delegated_vars + "/" + "logs"

        if not os.path.exists(custom_path):
           os.makedirs(custom_path)

        path = os.path.join(custom_path, "log_" + delegated_vars + ".log")
        if msg == None:
            msg = u""
        # msg = to_bytes(msg +'\n\n')
        if nl: 
            msg += u'\n'

        with codecs.open(path, "a", "utf-8") as stream:   # or utf-8
            stream.write(msg + u"\n")

        # with open(path, "ab") as fd:
        #     fd.write(msg.encode("UTF-8"))

    def v2_runner_on_failed(self, result, ignore_errors=False):

        delegated_vars = result._result.get('_ansible_delegated_vars', None)

        self._clean_results(result._result, delegated_vars)

        if self._play.strategy == 'free' and self._last_task_banner != result._task._uuid:
            self._print_task_banner(result._task)

        self._handle_exception(result._result)
        self._handle_warnings(result._result)

        if result._task.loop and 'results' in result._result:
            self._process_items(result)

        else:
            if delegated_vars:
                self._display.display("fatal: [%s -> %s]: FAILED! => %s" % (result._host.get_name(), delegated_vars['ansible_host'],
                                                                            self._dump_results(result._result)), color=C.COLOR_ERROR)
            else:
                self._display.display("fatal: [%s]: FAILED! => %s" % (result._host.get_name(), self._dump_results(result._result)), color=C.COLOR_ERROR)

        if ignore_errors:
            self._display.display("...ignoring", color=C.COLOR_SKIP)

        banner = self._print_task_banner(result._task, False)
        self.record_msg_per_host(banner, result._host.get_name(), False)
        self.record_msg_per_host(msg, result._host.get_name())

    def v2_runner_on_ok(self, result):

        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        # self._display.banner(result._t)
        marker = "write_log" in result._task.tags
        # self._display.banner(str("write_log" in result._task.tags))
        if marker:
            if self._play.strategy == 'free' and self._last_task_banner != result._task._uuid:
                # if not "write_log" in result._task._tags
                # 	return 0
                self._print_task_banner(result._task)
                # with open("/home/toor/Desktop/testing", "ab") as fd:
                #     fd.write(print(json.dumps(banner, indent = 4)))
    # ````````````self.record_msg_per_host(banner, result._host.get_name())
            if isinstance(result._task, TaskInclude):
                return
            elif result._result.get('changed', False):
                if delegated_vars:
                    msg = "changed: [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
                else:
                    msg = "changed: [%s]" % result._host.get_name()
                color = C.COLOR_CHANGED
            else:
                if delegated_vars:
                    msg = "ok: [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
                else:
                    msg = "ok: [%s]" % result._host.get_name()
                color = C.COLOR_OK

            self._handle_warnings(result._result)

            if result._task.loop and 'results' in result._result:
                self._process_items(result)
            else:
                self._clean_results(result._result, result._task.action)

                if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
                    msg += " => %s" % (self._dump_results(result._result),)
                self._display.display(msg, color=color)

            banner = self._print_task_banner(result._task, False)
            self.record_msg_per_host(banner, result._host.get_name(), False)
            self.record_msg_per_host(msg, result._host.get_name())

            # fd = VariableManager()
            # res = fd._get_magic_variables( self._play, self._host, self,_task,None,  )
            # with open("/home/toor/Desktop/testing", "ab") as fd:
            #     fd.write(print(json.dumps(BASE_DIR, indent = 4)))

    def v2_runner_on_skipped(self, result):
        msg = u''
        if self._plugin_options.get('show_skipped_hosts', C.DISPLAY_SKIPPED_HOSTS):  # fallback on constants for inherited plugins missing docs

            self._clean_results(result._result, result._task.action)

            if self._play.strategy == 'free' and self._last_task_banner != result._task._uuid:
                self._print_task_banner(result._task)

            if result._task.loop and 'results' in result._result:
                self._process_items(result)
            else:
                msg = "skipping: [%s]" % result._host.get_name()
                if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
                    msg += " => %s" % self._dump_results(result._result)
                self._display.display(msg, color=C.COLOR_SKIP)

        banner = self._print_task_banner(result._task, False)
        self.record_msg_per_host(banner, result._host.get_name(), False)
        self.record_msg_per_host(msg, result._host.get_name())


    def v2_runner_on_unreachable(self, result):
        if self._play.strategy == 'free' and self._last_task_banner != result._task._uuid:
            self._print_task_banner(result._task)
        msg = u''
        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        if delegated_vars:
            msg = "fatal: [%s -> %s]: UNREACHABLE! => %s" % (result._host.get_name(), delegated_vars['ansible_host'], self._dump_results(result._result))
            self._display.display(msg, color=C.COLOR_UNREACHABLE)
        else:
            msg = "fatal: [%s]: UNREACHABLE! => %s" % (result._host.get_name(), self._dump_results(result._result))
            self._display.display(msg, color=C.COLOR_UNREACHABLE)

        banner = self._print_task_banner(result._task, False)
        self.record_msg_per_host(banner, result._host.get_name(), False)
        self.record_msg_per_host(msg, result._host.get_name())



    def v2_playbook_on_no_hosts_matched(self):
        self._display.display("skipping: no hosts matched", color=C.COLOR_SKIP)

    def v2_playbook_on_no_hosts_remaining(self):
        self._display.banner("NO MORE HOSTS LEFT")

    def v2_playbook_on_task_start(self, task, is_conditional):
        # self._display.banner("\n".join(dir(task)))

        if self._play.strategy != 'free':
            self._print_task_banner(task)


    def _print_task_banner(self, task, disp = True):
        marker = "write_log" in task.tags

        if not marker:
            return u""
        else:
        # args can be specified as no_log in several places: in the task or in
        # the argument spec.  We can check whether the task is no_log but the
        # argument spec can't be because that is only run on the target
        # machine and we haven't run it thereyet at this time.
        #
        # So we give people a config option to affect display of the args so
        # that they can secure this if they feel that their stdout is insecure
        # (shoulder surfing, logging stdout straight to a file, etc).
        # msg = ''
        # self._display.banner(str(task.__dict__))
            args = u''
            if not task.no_log and C.DISPLAY_ARGS_TO_STDOUT:
                args = u', '.join(u'%s=%s' % a for a in task.args.items())
                args = u' %s' % args

            msg = u"TASK [%s%s] " % (task.get_name().strip(), args)
            # with codecs.open("/home/toor/Desktop/testing", "a", "utf-8") as stream:   # or utf-8
            #     stream.write(msg + u"\n")

            # with codecs.open(temp_path, "a", "utf-8") as stream:   # or utf-8
            #     stream.write(msg.ljust(100, "*")+ u"\n")


            # with open("/home/toor/Desktop/testing", "ab") as fd:
            #     fd.write(msg)
            if disp:
                self._display.banner(msg[:-1])
            # self.record_msg_per_host(msg, 'localhost')

            if self._display.verbosity >= 2:
                path = task.get_path()
                if path and disp:
                    self._display.display(u"task path: %s" % path, color=C.COLOR_DEBUG)


            self._last_task_banner = task._uuid
        # self._display.banner(str("write_log" in task.tags))
        # if marker = "write_log" in task.tags
        # self._display.banner(str("write_log" in result._task.tags))
            # return msg
        # else:
            # return u""

    def v2_playbook_on_cleanup_task_start(self, task):
        self._display.banner("CLEANUP TASK [%s]" % task.get_name().strip())

    def v2_playbook_on_handler_task_start(self, task):
        self._display.banner("RUNNING HANDLER [%s]" % task.get_name().strip())

    def v2_playbook_on_play_start(self, play):
        name = play.get_name().strip()
        msg = u""
        if not name:
            msg = u"PLAY"
        else:
            msg = u"PLAY [%s]" % name

        with codecs.open(temp_path, "a", "utf-8") as stream:   # or utf-8
            stream.write(msg + u"\n\n")

        self._play = play
        self._display.banner(str(self._play))

    def v2_on_file_diff(self, result):
        if result._task.loop and 'results' in result._result:
            for res in result._result['results']:
                if 'diff' in res and res['diff'] and res.get('changed', False):
                    diff = self._get_diff(res['diff'])
                    if diff:
                        self._display.display(diff)
                        self.record_msg_per_host(diff, result._host.get_name())

        elif 'diff' in result._result and result._result['diff'] and result._result.get('changed', False):
            diff = self._get_diff(result._result['diff'])
            if diff:
                self._display.display(diff)
                self.record_msg_per_host(diff, result._host.get_name())

    def v2_runner_item_on_ok(self, result):
        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        self._clean_results(result._result, result._task.action)
        if isinstance(result._task, TaskInclude):
            return
        elif result._result.get('changed', False):
            msg = 'changed'
            color = C.COLOR_CHANGED
        else:
            msg = 'ok'
            color = C.COLOR_OK

        if delegated_vars:
            msg += ": [%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
        else:
            msg += ": [%s]" % result._host.get_name()

        msg += " => (item=%s)" % (self._get_item(result._result),)

        if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
            msg += " => %s" % self._dump_results(result._result)

        self._display.display(msg, color=color)
        self.record_msg_per_host(msg, result._host.get_name())

    def v2_runner_item_on_failed(self, result):

        delegated_vars = result._result.get('_ansible_delegated_vars', None)
        self._clean_results(result._result, result._task.action)
        self._handle_exception(result._result)

        msg = "failed: "
        if delegated_vars:
            msg += "[%s -> %s]" % (result._host.get_name(), delegated_vars['ansible_host'])
        else:
            msg += "[%s]" % (result._host.get_name())

        self._handle_warnings(result._result)
        self._display.display(msg + " (item=%s) => %s" % (self._get_item(result._result), self._dump_results(result._result)), color=C.COLOR_ERROR)
        self.record_msg_per_host(msg, result._host.get_name())

    def v2_runner_item_on_skipped(self, result):
        if self._plugin_options.get('show_skipped_hosts', C.DISPLAY_SKIPPED_HOSTS):  # fallback on constants for inherited plugins missing docs
            self._clean_results(result._result, result._task.action)
            msg = "skipping: [%s] => (item=%s) " % (result._host.get_name(), self._get_item(result._result))
            if (self._display.verbosity > 0 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
                msg += " => %s" % self._dump_results(result._result)
            self._display.display(msg, color=C.COLOR_SKIP)
            self.record_msg_per_host(msg, result._host.get_name())

    def v2_playbook_on_include(self, included_file):
        msg = 'included: %s for %s' % (included_file._filename, ", ".join([h.name for h in included_file._hosts]))
        self._display.display(msg, color=C.COLOR_SKIP)
        self.record_msg_per_host(msg, msg.split()[-1])

    def v2_playbook_on_stats(self, stats):
        self._display.banner("PLAY RECAP")

        hosts = sorted(stats.processed.keys())
        for h in hosts:
            t = stats.summarize(h)

            self._display.display(u"%s : %s %s %s %s" % (
                hostcolor(h, t),
                colorize(u'ok', t['ok'], C.COLOR_OK),
                colorize(u'changed', t['changed'], C.COLOR_CHANGED),
                colorize(u'unreachable', t['unreachable'], C.COLOR_UNREACHABLE),
                colorize(u'failed', t['failures'], C.COLOR_ERROR)),
                screen_only=True
            )

            self._display.display(u"%s : %s %s %s %s" % (
                hostcolor(h, t, False),
                colorize(u'ok', t['ok'], None),
                colorize(u'changed', t['changed'], None),
                colorize(u'unreachable', t['unreachable'], None),
                colorize(u'failed', t['failures'], None)),
                log_only=True
            )

        self._display.display("", screen_only=True)

        # print custom stats
        if self._plugin_options.get('show_custom_stats', C.SHOW_CUSTOM_STATS) and stats.custom:  # fallback on constants for inherited plugins missing docs
            self._display.banner("CUSTOM STATS: ")
            # per host
            # TODO: come up with 'pretty format'
            for k in sorted(stats.custom.keys()):
                if k == '_run':
                    continue
                self._display.display('\t%s: %s' % (k, self._dump_results(stats.custom[k], indent=1).replace('\n', '')))

                # print per run custom stats
            if '_run' in stats.custom:
                self._display.display("", screen_only=True)
                self._display.display('\tRUN: %s' % self._dump_results(stats.custom['_run'], indent=1).replace('\n', ''))
        self._display.display("", screen_only=True)

    def v2_playbook_on_start(self, playbook):
        # self._display.banner("\n".join(dir(playbook)))
        if self._display.verbosity > 1:
            from os.path import basename
            msg = self._display.banner("PLAYBOOK: %s" % basename(playbook._file_name))

        if self._display.verbosity > 3:
            # show CLI options
            if self._options is not None:
                for option in dir(self._options):
                    if option.startswith('_') or option in ['read_file', 'ensure_value', 'read_module']:
                        continue
                    val = getattr(self._options, option)
                    if val and self._display.verbosity > 3:
                        self._display.display('%s: %s' % (option, val), color=C.COLOR_VERBOSE, screen_only=True)

    def v2_runner_retry(self, result):
        task_name = result.task_name or result._task
        msg = "FAILED - RETRYING: %s (%d retries left)." % (task_name, result._result['retries'] - result._result['attempts'])
        if (self._display.verbosity > 2 or '_ansible_verbose_always' in result._result) and '_ansible_verbose_override' not in result._result:
            msg += "Result was: %s" % self._dump_results(result._result)
        self._display.display(msg, color=C.COLOR_DEBUG)
        self.record_msg_per_host(msg, result._host.get_name())


    def v2_playbook_on_notify(self, handler, host):
        if self._display.verbosity > 1:
            self._display.display("NOTIFIED HANDLER %s for %s" % (handler.get_name(), host), color=C.COLOR_VERBOSE, screen_only=True)
            self.record_msg_per_host(u"NOTIFIED HANDLER %s for %s" % (handler.get_name(), host), host)
