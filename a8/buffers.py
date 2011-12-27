# -*- coding: utf-8 -*- 
# (c) 2005-2011 PIDA Authors
# vim: ft=python sw=2 ts=2 sts=2 tw=80


"""Buffer list."""


import os

import gtk, gtk.gdk
from pygtkhelpers.ui import objectlist

from a8 import resources, lists


class Buffer(lists.ListItem):
  """Loaded buffer."""

  MARKUP_TEMPLATE = '<b>{0}</b>\n<span size="xx-small">{1}</span>'

  def __init__(self, filename):
    self.filename = filename
    self.dirname = os.path.dirname(filename)
    self.basename = os.path.basename(filename)

  @property
  def markup_args(self):
    """Display in the buffer list."""
    return (self.basename, self.dirname)


class BufferManager(lists.ListView):
  """Buffer list."""

  LABEL = 'Buffers'
  ICON  = 'page_white_stack.png'

  def create_ui(self):
    lists.ListView.create_ui(self)
    self.filenames = {}

  def append(self, filename):
    if filename not in self.filenames:
      self.filenames[filename] = buf = Buffer(filename)
      self.items.append(buf)
    if not self.items.selected_item or self.items.selected_item.filename != filename:
      self.items.selected_item = self.filenames[filename]

  def on_items__item_activated(self, items, item):
    self.model.vim.open_file(item.filename)
    self.model.vim.grab_focus()

