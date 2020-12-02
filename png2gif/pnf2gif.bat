ffmpeg -framerate 1 -i kmeans%1d.png -c:v libx264 -r 30 temp.mp4
ffmpeg -i temp.mp4 -filter_complex "[0:v] palettegen" template.png
ffmpeg -i temp.mp4 -i template.png -r 30 -filter_complex "[0:v][1:v] paletteuse" kmeans.gif
