# Window Functions
self.bind('Ctrl+X, Ctrl+C', 'std', self.exit)

self.bind('Ctrl+P', 'bufferstd', self.select_all)

# MiniBuffer Functions
#self.bind('Ctrl+X, Ctrl+F', 'bufferstd', self.minibuffer_open_file_hook)


# Stack Functions
self.bind('Ctrl+X, O', 'bufferstd', self.focus_next_stack)
self.bind('Ctrl+X, 2', 'bufferstd', self.new_vstack)
self.bind('Ctrl+X, 3', 'bufferstd', self.new_hstack)
self.bind('Ctrl+X, Right', 'bufferstd', self.next_buffer)
self.bind('Ctrl+X, Left', 'bufferstd', self.previous_buffer)

# Cursor Movement
self.bind('Left', 'std', self.move_cursor_char_left)
self.bind('Right', 'std', self.move_cursor_char_right)
self.bind('Up', 'std', self.move_cursor_line_up)
self.bind('Down', 'std', self.move_cursor_line_down)

self.bind('Ctrl+Left', 'std', self.move_cursor_word_left)
self.bind('Ctrl+Right', 'std', self.move_cursor_word_right)
self.bind('Ctrl+Up', 'std', self.move_cursor_block_up)
self.bind('Ctrl+Down', 'std', self.move_cursor_block_down)

self.bind('Ctrl+E', 'std', self.move_cursor_line_end)
self.bind('Ctrl+A', 'std', self.move_cursor_line_start)
self.bind('Ctrl+Shift+E', 'std', self.move_cursor_line_end_mark)
self.bind('Ctrl+Shift+A', 'std', self.move_cursor_line_start_mark)

# Mark Mode
self.bind('Ctrl+Space', 'std', self.toggle_mark_mode)
