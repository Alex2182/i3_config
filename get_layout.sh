layouts=$(setxkbmap -query | grep layout | xargs | cut -d ':' -f2)
pos=$(xset -q | grep LED | cut -d ':' -f4 | xargs | cut -c 5-5)
echo $layouts | cut -d ',' -f $(( $pos +1 )) | tr '[:lower:]' '[:upper:]'
