while :
	do
		if pgrep -x "cmus" > /dev/null
		then
    			python3 /home/chaspen/.config/polybar/cmus.py
		else
			echo ""
		fi
	done
fi
set -e
