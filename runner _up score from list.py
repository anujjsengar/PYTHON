#Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(0,arr.count(max(arr))):
        arr.remove(max(arr))
    print(max(arr))
