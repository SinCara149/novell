init python:




    class Scene(object):
        
        def __init__(self, id, *frames, **properties):
            
            self.id = id
            self.replay = properties.pop('replay', False)
            self.frames = []
            
            for i,img in enumerate(frames):
                self.frames.append(img)




    class AnimationController(renpy.Displayable):
        
        def __init__(self, state_variable, *scenes, **properties):
            super(AnimationController, self).__init__(**properties)
            
            self.fps = properties.pop('fps', 30)
            self.state_variable = state_variable
            self.scenes = dict()
            self.current_scene = None
            self.current_frame_index = -1
            
            for i,x in enumerate(scenes):
                self.scenes[x.id] = x
        
        
        def _get_next_scene_id(self):
            x = globals()[self.state_variable]
            if type(x) is list:
                if len(x) == 0:
                    return None
                id = x.pop(0)
                if len(x) == 0:
                    globals()[self.state_variable] = id
                return id
            else:
                return x
        
        
        def _get_next_frame(self):
            
            
            if self.current_scene is None:
                first_scene_id = self._get_next_scene_id()
                if first_scene_id is None:
                    return (None, -1) 
                return (self.scenes[first_scene_id], 0) 
            
            
            idx = self.current_frame_index + 1
            if idx < len(self.current_scene.frames):
                return (self.current_scene, idx) 
            
            
            next_scene_id = self._get_next_scene_id()
            if next_scene_id is None:
                return (None, -1) 
            if next_scene_id != self.current_scene.id:
                return (self.scenes[next_scene_id], 0) 
            
            
            if self.current_scene.replay:
                return (self.current_scene, 0) 
            
            
            return (self.current_scene, self.current_frame_index)
        
        
        def render(self, width, height, st, at):
            
            delay = 1.0 / float(self.fps)
            t = at % delay
            renpy.redraw(self, delay - t)
            
            scene, frame_index = self._get_next_frame()
            if scene is None:
                return renpy.Render(width, height)
            
            if self.current_scene is None or scene.id != self.current_scene.id:
                self.current_scene = scene
            
            if frame_index != self.current_frame_index:
                self.current_frame_index = frame_index
            
            img = scene.frames[frame_index]
            rv = renpy.render(renpy.displayable(img), width, height, st, at)
            return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
