# coding=utf-8
# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from pants.base.exceptions import TaskError
from pants.pantsd.pants_daemon import PantsDaemon
from pants.pantsd.process_manager import ProcessManager
from pants.task.task import Task


class PantsDaemonKill(Task):
  """Terminate the pants daemon."""

  def execute(self):
    try:
      PantsDaemon.Factory.create(self.context.options, full_init=False).terminate()
    except ProcessManager.NonResponsiveProcess as e:
      raise TaskError('failure while terminating pantsd: {}'.format(e))
