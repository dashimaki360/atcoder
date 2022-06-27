while true; do
    python3 ./generate.py > input.txt
    ans1=$(python main.py < input.txt)
    ans2=$(python naive.py < input.txt)
    if [ "$ans1" != "$ans2" ]; then
        echo "Wrong Answer"
        echo "main.py", $ans1
        echo "naive.py", $ans2
        cat input.txt
        exit
    fi
done