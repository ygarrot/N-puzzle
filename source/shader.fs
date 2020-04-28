#version 330

uniform float time;
uniform int n;
vec2 resolution = vec2(800, 600);
uniform int grid[1024];

void main()
{
    vec2 uv = (gl_FragCoord.xy-0.5*resolution.xy)/resolution.y;
    vec3 col = vec3(0);

    vec2 guv = fract(vec2(uv + 0.5 + 1. / float(n)) * float(n));
    vec2 id = floor(vec2(uv + 0.5 + 1. / float(n)) * float(n));

    float m = 0.;

    if (id.x > 0. && id.x <= float(n) && id.y > 0. && id.y <= float(n))
    {
    	col.gb = smoothstep(1., float(n), abs(mod(id + time, float(n)) - float(n) / 2.) + 1.);
        float d = length(guv - 0.5);
        float dist = length(id) * 10.;
        float r = mix(.0001, .2, (sin(time) * 0.2 + 1.2) * float(grid[int(float(n) - id.y) * n + int(id.x - 1.)]) / float(n * n));
        m += 1 - smoothstep(r, r * .1, d);
    }
    col.xyz += vec3(m);
    gl_FragColor = vec4(col,1.0);
}
