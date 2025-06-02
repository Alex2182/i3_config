function fish_right_prompt -d "Write out the right prompt"
	if [ "$CMD_DURATION" -lt 5000 ]
        	printf '󱦟 %s ms' $CMD_DURATION
    	else if [ "$CMD_DURATION" -lt 60000 ]
        	printf '󱦟 %s s' (math -s1 $CMD_DURATION/1000)
    	else if [ "$CMD_DURATION" -lt 3600000 ]
        	set_color -b yellow
        	printf '󱦟 %s m' (math -s0 $CMD_DURATION/60000)
    	else
        	set_color -b red
        	printf '󱦟 %s h' (math -s0 $CMD_DURATION/3600000)
    end
    set_color normal
    # printf '%s sec' (math -s0 $CMD_DURATION/1000) 
end
