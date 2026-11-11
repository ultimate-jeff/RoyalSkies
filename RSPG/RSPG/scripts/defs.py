from scripts.imports import *

class Vector:

    def update(self):
            self.angle,self.speed = util.couculate_angle_dist(self.dx,self.dy)

    def __init__(self,x,y,dx,dy):
        self.x,self.y = x,y
        self.dx,self.dy = dx,dy
        self.update()

    def set_angle_speed(self,angle:"float",speed:"float"):
        self.angle,self.speed = angle,speed
        self.dx,self.dy = util.couculate_dx_dy(speed,angle)
    def get_angle_speed(self):
        return self.angle,self.speed
    def set_dx_dy(self,dx,dy):
        self.dx,self.dy = dx,dy
        self.angle,self.speed = self.get_angle_speed()
    def get_dx_dy(self):
        return (self.dx,self.dy)

    def update_pos(self):
        self.x += self.dx
        self.y += self.dy

class Plane(sp.Layer):
    def on_collide(self):
        self.health -= self.config.get("crash_damage",1) * self.dt

    def _setup(self,x,y,angle,tags):
        self.vect = Vector(x,y,0,0) # init vector
        self.vect.set_angle_speed(angle,self.config.get("min_speed",0))

        hb_size = self.config.get("hitbox_size",[0,0]) # init hitbox
        self.hitbox = sp.Hitbox(x,y,hb_size[0],hb_size[1],angle,tags=tags,on_collide=self.on_collide)

        img_size = self.config.get("image_size",[0,0]) # init image
        size = self.config.get("layer_size",[50,50])
        rx = (size[0]-img_size[0]) / 2
        ry = (size[1]-img_size[1]) / 2
        self.render = sp.Render(rx,ry,img_size[0],img_size[1],0,loader.image(f"assets/planes/images/{self.config.get("image_name","error")}.png"),tags)

    def __init__(self,pt:"str",x:"float",y:"float",angle:"float", tags=None):
        self.pt = pt
        self.config = loader.read(f"assets/planes/stats/{pt}.json")
        self.dt = 0
        self.health = self.config.get("max_health",50)

        self._setup(x,y,angle,tags)

        size = self.config.get("layer_size",[50,50]),
        super().__init__(
            size[0],
            size[1],
            x, y,
            angle, 
            loader.image(f"assets/planes/images/{pt}.png"), 
            (0,0,0,0), 
            fill_every_frame=False, 
            tags=tags
        )
        self.add_obj(self.render)

    def check_speed(self,speed):
        if speed > self.config.get("max_speed",1):
            speed -= self.config.get("acceleration",1)
        elif speed < self.config.get("min_speed",0.9):
            speed += self.config.get("acceleration",1)
        self.vect.speed = speed
        return speed

    def run_ai(self):
        pass

    def take_input(self,keypressed:"tuple",keydown:"dict"={}):
        if keypressed[pygame.K_a]:
            self.vect.set_angle_speed(
                self.vect.angle + self.config.get("turn_acceleration",1),
                self.check_speed(self.vect.speed)
            )
        elif keypressed[pygame.K_d]:
            self.vect.set_angle_speed(
                self.vect.angle - self.config.get("turn_acceleration",1),
                self.check_speed(self.vect.speed)
            )
        if keypressed[pygame.K_w]:
            self.vect.set_angle_speed(
                self.vect.angle,
                self.check_speed(self.vect.speed + 1)
            )
        elif keypressed[pygame.K_s]:
            self.vect.set_angle_speed(
                self.vect.angle,
                self.check_speed(self.vect.speed - 1)
            )

    def _update_(self, events):
        self._update_objs(events)
        if self.tags.get("controlor","bot") == "player":
            self.take_input(keypressed=pygame.key.get_pressed())
        else:
            self.run_ai()
        self._handle_events(events)

class AI_plane(Plane):
    def __init__(self, pt, x, y, angle, tags=None):
        super().__init__(pt, x, y, angle, tags)

    def run_ai(self):
        return super().run_ai()
    