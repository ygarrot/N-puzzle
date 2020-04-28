#include <stdio.h>
#include <string.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include "ogldev_math_3d.h"
#include <iostream>
#include <sstream>
#include <cmath>

GLuint VBO;
GLuint gridLocation;
GLuint nLocation;
GLuint timeLocation;

const char* pVSFileName = "source/shader.vs";
const char*	pFSFileName = "source/shader.fs";
const char*	pGridFileName = "./test/visu.txt";

static void RenderSceneCB()
{
	glClear(GL_COLOR_BUFFER_BIT);

    string grid_file;

	if (!ReadFile(pGridFileName, grid_file))
        exit(1);
	static float time = 0.0f;
	time += 0.03;

    stringstream ssin(grid_file);
    string token;
    string token2;
    int garbage[1024];
    int i = 0;
    int j = 0;
    int x = 0, y = 0;
    while (std::getline(ssin, token, '\n'))
    {
        j = 0;
        stringstream ssin2(token);
        while (ssin2.good())
        {
            ssin2 >> garbage[j];
            j++;
            if (j > x)
                x = j;
        }
        i++;
        if (i > y)
            y = i;
    }
    int n = (int)sqrt(x);
    int grid[y][x];
    stringstream ssin3(grid_file);
    i = 0;
    while (ssin3.good() && i < x * y)
    {
        ssin3 >> grid[(int)(i / x)][i % x];
        i++;
    }
    glUniform1f(timeLocation, time);
	glUniform1i(nLocation, n);
    if ((int)time < sizeof(grid) / sizeof(*grid))
       glUniform1iv(gridLocation, n * n, grid[(int)time]);
    else
      exit(1);
	glEnableVertexAttribArray(0);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);

	// first GL_POINT or GL_TRIANGLES
	// second start of draw
	// third number of vertices to draw
	glDrawArrays(GL_QUADS, 0, 4);

	glDisableVertexAttribArray(0);

	glutSwapBuffers();
}

static void InitializeGlutCallbacks(void)
{
	glutDisplayFunc(RenderSceneCB);
	glutIdleFunc(RenderSceneCB);
}

static void CreateVertexBuffer(void)
{
	Vector3f Vertices[4];
	Vertices[0] = Vector3f(-1.0f, -1.0f, 0.0f);
	Vertices[1] = Vector3f(1.0f, -1.0f, 0.0f);
	Vertices[2] = Vector3f(1.0f, 1.0f, 0.0f);
	Vertices[3] = Vector3f(-1.0f, 1.0f, 0.0f);

	glGenBuffers(1, &VBO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, sizeof(Vertices), Vertices, GL_STATIC_DRAW);
}

static void AddShader(GLuint ShaderProgram, const char* pShaderText, GLenum ShaderType)
{
	GLuint ShaderObj = glCreateShader(ShaderType);

	if (ShaderObj == 0)
	{
		fprintf(stderr, "Error creating shader type %d\n", ShaderType);
		exit(0);
	}

	const GLchar* p[1];
	p[0] = pShaderText;
	GLint Lengths[1];
	Lengths[0] = strlen(pShaderText);
	glShaderSource(ShaderObj, 1, p, Lengths);
	glCompileShader(ShaderObj);
	GLint success;
	glGetShaderiv(ShaderObj, GL_COMPILE_STATUS, &success);
	if (!success)
	{
		GLchar InfoLog[1024];
		glGetShaderInfoLog(ShaderObj, 1024, NULL, InfoLog);
		fprintf(stderr, "Error compiling shader type %d: '%s'\n", ShaderType, InfoLog);
		exit(1);
	}

	glAttachShader(ShaderProgram, ShaderObj);

}

static void CompileShaders()
{
	GLuint ShaderProgram = glCreateProgram();

	if (ShaderProgram == 0)
	{
		fprintf(stderr, "Error creating shader program\n");
		exit(1);
	}

	string vs;
	string fs;

	if (!ReadFile(pVSFileName, vs))
		exit(1);

	if (!ReadFile(pFSFileName, fs))
		exit(1);

	AddShader(ShaderProgram, vs.c_str(), GL_VERTEX_SHADER);
	AddShader(ShaderProgram, fs.c_str(), GL_FRAGMENT_SHADER);

	GLint Success = 0;
	GLchar ErrorLog[1024] = { 0 };

	glLinkProgram(ShaderProgram);
	glGetProgramiv(ShaderProgram, GL_LINK_STATUS, &Success);
	if (Success == 0)
	{
		glGetProgramInfoLog(ShaderProgram, sizeof(ErrorLog), NULL, ErrorLog);
		fprintf(stderr, "Error linking shader program : '%s'\n", ErrorLog);
		exit(1);
	}

	glValidateProgram(ShaderProgram);
	glGetProgramiv(ShaderProgram, GL_VALIDATE_STATUS, &Success);
	if (!Success)
	{
		glGetProgramInfoLog(ShaderProgram, sizeof(ErrorLog), NULL, ErrorLog);
		fprintf(stderr, "Invalid shader program '%s'\n", ErrorLog);
		exit(1);
	}

	glUseProgram(ShaderProgram);
	gridLocation = glGetUniformLocation(ShaderProgram, "grid");
	assert(gridLocation != 0xFFFFFFFF);
	nLocation = glGetUniformLocation(ShaderProgram, "n");
	assert(nLocation != 0xFFFFFFFF);
	timeLocation = glGetUniformLocation(ShaderProgram, "time");
	assert(timeLocation != 0xFFFFFFFF);
}

int			main(int argc, char **argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowSize(800, 600);
	glutCreateWindow("N-Puzzle");
	//glutFullScreen();

	InitializeGlutCallbacks();

	// Must be done after glut is initialized !
	GLenum res = glewInit();
	if (res != GLEW_OK)
	{
		fprintf(stderr, "Error : '%s'\n", glewGetErrorString(res));
		return (1);
	}

	printf("GL version: %s\n", glGetString(GL_VERSION));

	glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

	CreateVertexBuffer();

	CompileShaders();

	glutMainLoop();
	return (0);
}
