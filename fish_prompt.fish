function fish_prompt
	#if not set -q VIRTUAL_ENV_DISABLE_PROMPT
	#        set -g VIRTUAL_ENV_DISABLE_PROMPT true
	#end
	set -l color_1 green
	#purple
	set -l color_2 white
   	set_color normal
	printf '╭─'
	# set_color $fish_color_cwd
	#printf '%s [%s]' (prompt_pwd) (date +%T)
	#set_color normal
	#\uE0B6
  	printf '%s%s%s' (set_color -b normal $color_1) \uE0B6 (set_color normal)
	set_color -b $color_1 $color_2
        printf '󱑃 %s%s' (date "+%H:%M:%S") (set_color -b normal)
  	printf '%s\uE0B4%s' (set_color -b $color_2 $color_1)
        printf '%s 󰉒 %s' (set_color -b white $color_1) $PWD
  	printf '%s%s%s\n' (set_color -b normal $color_2) \uE0B4 (set_color -b normal normal)
	# set_color -b normal

        # Line 2
	printf '╰─>'
	# printf '󱞩'
	# set_color normal
end
