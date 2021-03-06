from ursina import Shader


camera_grayscale_shader = Shader(
vertex='''
#version 430

uniform mat4 p3d_ViewMatrixInverse;
in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;
out vec2 uv;

void main() {
  gl_Position = p3d_ViewMatrixInverse  * p3d_Vertex;
  uv = p3d_MultiTexCoord0;
}
''',

fragment='''
#version 430

uniform sampler2D tex;
in vec2 uv;
out vec4 color;

void main() {
    vec3 rgb = texture(tex, uv).rgb;
    float gray = (rgb.x + rgb.y + rgb.z)/3;
    color = vec4(gray, gray, gray, 1.0);
}

''',
geometry='')



if __name__ == '__main__':
    from ursina import *
    app = Ursina()

    e = Entity(model='sphere', color=color.orange)
    e = Entity(model='cube', y=-1)
    camera.shader = camera_grayscale_shader
    # camera.set_shader_input('contrast', 1)
    EditorCamera()

    def input(key):
        if key == 'space':
            if camera.shader:
                camera.shader = None
            else:
                camera.shader = camera_grayscale_shader


    app.run()
