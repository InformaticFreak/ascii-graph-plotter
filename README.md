
# ASCII Graph Plotter

[![GitHub License](https://img.shields.io/badge/license-MIT-green)](LICENSE.txt)&nbsp;
[![Python Version](https://img.shields.io/badge/python-3-blue)](https://www.python.org/downloads/)&nbsp;
[![GitHub release](https://img.shields.io/github/v/release/InformaticFreak/ascii-graph-plotter)](https://github.com/InformaticFreak/ascii-graph-plotter/releases/tag/2021.1)&nbsp;
[![CodeFactor](https://www.codefactor.io/repository/github/informaticfreak/ascii-graph-plotter/badge/main)](https://www.codefactor.io/repository/github/informaticfreak/ascii-graph-plotter/overview/main)&nbsp;
![visitors](https://visitor-badge.laobi.icu/badge?page_id=informaticfreak/ascii-graph-plotter)&nbsp;
[![Example: My use case](https://img.shields.io/badge/example-my%20use%20case-green)](http://tubaf.informatic-freak.de/hoehere-mathematik-fuer-ingenieure-1.php#epsilon-delta-kriterium-der-stetigkeit)&nbsp;

Plots the graph of a function with ASCII characters.

See the change log [here](CHANGELOG.md).

Developed by InformaticFreak (c) 2021

## How to use

```
py main.py [function: str] [scale: float,float] [origin: int,int] [size: int,int] [discontinuous: bool] [precision: bool] [ascii_only: bool]
```

| Parameter | Type | Default value | Description |
|---|---|---|---|
| *function* | `str` | | Defines the function |
| *scale* | `float,float` | `0.1,10` | Scales the graph in x,y direction |
| *origin* | `int,int` | `40,20` calculated by `(scale-1)/2` | Sets the origin of the plot to the list index x,y |
| *size* | `int,int` | `81,41` | Sets the size x,y in characters of the plot |
| *discontinuous* | `bool` | `false` | Specifies if the graph should be plotted discontinuously |
| *precision* | `bool` | `false` | Specifies if the graph should be plottet with thinner characters oriented at the angle at the point |
| *ascii_only* | `bool` | `false` | Specifies whether the graph should be plotted with thinner characters, depending on the slope at each point |

### Built-In Functions

- `sin`, `cos`, `tan`, `cot`
- `asin`, `acos`, `atan`, `acot`
- `degrees`, `radian`
- `log`, `sign`, `sqrt`

### Constants

- `e`, `pi`

## Examples

- Specifie the scale in x direction as 0.2 and use the default scale in y direction of 10, so write `0.2,_`
- Set the x origin to the list index 5 and use the default y origin of list index 20, so write `5,_`
- Use the default x size of the plot of 81 and specifie the y size of the plot as 31, so write `_,31`
- Use the default for all other parameter, so do not write anything or use `_,_` for every single parameter

```
py main.py sin(x) 0.2,_ 5,_ _,31
```

The result plot contains the plotted graph of the function and in the first line all parameter values to reproduce it. Also, the entire plot is copied to the clipboard.

```
f(x)=sin(x) 0.2,10.0 5,14 81,31 0 0 0

     ▲                                                                           
     │                                                                           
     │                                                                           
     │                                                                           
     │      ███                            ███                             ███   
     ┤     █   █                          █   ██                         ██   █  
     │    █     █                        █      █                       █      █ 
     │   █       █                      █       █                       █       █
     │  █         █                     █        █                     █         
     │  █         █                    █          █                   █          
     ┤ █          █                   █           █                   █          
     │█            █                  █           █                   █          
     │█             █                 █            █                 █           
     │█             █                █              █               █            
┬────█────┬────┬────█────┬────┬────┬█───┬────┬────┬─█──┬────┬────┬──█─┬────┬────▸
    █┤               █              █               █               █            
    █│                █             █                █             █             
    █│                █            █                  █           █              
   █ │                 █          █                   █           █              
  █  │                  █         █                    █         █               
  █  ┤                  █        █                      █       █                
 █   │                  █       █                       █       █                
█    │                   █      █                        █     █                 
     │                    █    █                          █   █                  
     │                     ████                            ███                   
     ┤                                                                           
     │                                                                           
     │                                                                           
     │                                                                           
     │                                                                           
     ┤                                                                           
```

- Set the discontinuous Parameter to default, so write `_`
- Now specifie the precision Parameter to true, so write `1`, `true` or `True`

```
py main.py f(x)=sin(x) 0.2,10 5,14 81,31 _ 1
```

The plotted graph of the function now has thinner lines and a suitable character, depending on the slope of the the respective point.

```
f(x)=sin(x) 0.2,10.0 5,14 81,31 0 1 0

     ▲                                                                           
     │                                                                           
     │                                                                           
     │                                                                           
     │      --\                            --\                             --\   
     ┤     /   \                          /   -\                         -/   \  
     │    /     \                        /      |                       /      \ 
     │   /       \                      /       \                       |       -
     │  /         |                     |        \                     /         
     │  |         |                    /          |                   /          
     ┤ /          \                   /           |                   |          
     │/            \                  |           \                   |          
     │|             |                 |            \                 /           
     │|             |                /              |               /            
┬────/────┬────┬────\────┬────┬────┬/───┬────┬────┬─|──┬────┬────┬──|─┬────┬────▸
    /┤               \              |               \               |            
    |│                |             |                \             /             
    |│                \            /                  |           /              
   / │                 \          /                   \           |              
  /  │                  |         |                    \         /               
  |  ┤                  |        /                      |       /                
 /   │                  \       /                       \       |                
/    │                   \      |                        \     /                 
     │                    \    /                          \   /                  
     │                     ---/                            --/                   
     ┤                                                                           
     │                                                                           
     │                                                                           
     │                                                                           
     │                                                                           
     ┤                                                                           
```
