
## Run the program

From this folder:

```bash
cd /home/ubuntu/pathfinding
python main.py
```

Then enter:
1. Map path (example: `maps/map_easy.txt`)
2. Algorithm (`astar` or `bfs`)

## Map format

Allowed symbols:
- `S` start
- `G` goal
- `.` open cell
- `#` wall

Each map must:
- be rectangular
- contain exactly one `S`
- contain exactly one `G`

## Example output

- Algorithm name
- Whether path was found
- Path length
- Nodes explored
- Rendered map with `*` path markers
