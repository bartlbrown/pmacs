# Fill out settings dict
self.settings['window_geometry'] = [1000, 1000, 1000, 1000]
self.settings['window_title'] = 'pmacs'
self.settings['scratch_message'] = 'Scratch\n'
self.settings['debug_message'] = 'Debug\n'
self.settings['stylesheet_path'] = self.THEMEDIR + 'default.qss'
self.settings['std_buffer_modes'] = ['std', 'bufferstd']
self.settings['std_minibuffer_modes'] = ['std']

# load modules
self.require('framestd')  # important frame functions - required
self.require('std')           # functions standard to all widgets
self.require('bufferstd')  # functions standard to all buffers
self.require('minibufferfile')
# load keybindings
self.eval_file(self.CONFIGDIR + 'keybindstd.pm')
