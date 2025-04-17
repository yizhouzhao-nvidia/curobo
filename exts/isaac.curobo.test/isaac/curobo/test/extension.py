import omni.ext
import omni.ui as ui


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print(f"[omni.hello.world] some_public_function was called with {x}")
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.hello.world] MyExtension startup")

        self._count = 0

        self._window = ui.Window("Curobot Isaac Sim 4.5 Test", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                ui.Label("Basic Tests", height=20)
                with ui.HStack():
                    ui.Button("Debug", height = 20, clicked_fn=self.debug)
    

    def on_shutdown(self):
        print("[omni.hello.world] MyExtension shutdown")
        
    def debug(self):
        print("[omni.hello.world] Debug button clicked")
