from OpenGL.GL import *
from OpenGL.GLUT import *
import math
import numpy as np

time = 0.
with open('./test/visu.txt') as f:
	content = f.read().splitlines()
line = []
for v in content:
	line.append(v.split())

print(line)



def create_shader(shader_type, source):
	shader = glCreateShader(shader_type)
	glShaderSource(shader, source)
	glCompileShader(shader)
	return shader

def timer(value):
	global time
	if time > 1000.:
		time = 0.
	else:
		time += .03
	glutPostRedisplay()
	glutTimerFunc(10, timer, 0)

def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glUniform1f(timeLocation, time)
	if int(time) < len(line) - 0:
		glUniform1iv(grid, n*n, np.array(line[int(time)]))
	else:
		quit()
	glRecti(-1, -1, 1, 1)
	glutSwapBuffers()

glutInit()
w = glutGet(GLUT_SCREEN_WIDTH)
h = glutGet(GLUT_SCREEN_HEIGHT)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(800, 600)
glutInitWindowPosition(400, 300)
glutCreateWindow("N-Puzzle solver")
glutDisplayFunc(draw)
fragment = create_shader(GL_FRAGMENT_SHADER, """
uniform float time;
uniform int n;
vec2 resolution = vec2(800, 600);
uniform int grid[36];

void main()
{
	//int []grid = int[9](1,2,3,4,5,6,7,8,0);
    for (int i = 0; i < n * n; i++)
        if (grid[i] == 0)
        {
            grid[i] = 0;
            break;
        }

    vec2 uv = (gl_FragCoord-.5*resolution.xy)/resolution.y;
    vec3 col = vec3(0);

    vec2 guv = fract(vec2(uv + 0.5 + 1. / float(n)) * float(n));
    vec2 id = floor(vec2(uv + 0.5 + 1. / float(n)) * float(n));

    float m = 0.;

    if (id.x > 0. && id.x <= float(n) && id.y > 0. && id.y <= float(n))
    {
    	col.gb = smoothstep(1., float(n), abs(mod(id + time, float(n)) - float(n) / 2.) + 1.);
        float d = length(guv - 0.5);
        float dist = length(id) * 10.;
        float r = mix(.0001, .5, (sin(time) * 0.2 + 1.2) * float(grid[int(float(n) - id.y) * n + int(id.x - 1.)]) / float(n * n));
        m += smoothstep(r, r * .1, d);
    }
    col += vec3(m);
    gl_FragColor = vec4(col,1.0);
}

""")
program = glCreateProgram()
glAttachShader(program, fragment)
glLinkProgram(program)
glutTimerFunc(100, timer, 0)
glUseProgram(program)
timeLocation = glGetUniformLocation(program, "time")
n = glGetUniformLocation(program, "n")
grid = glGetUniformLocation(program, "grid")
glUniform1i(n, int(math.sqrt(len(line[0]))))
glutMainLoop()
