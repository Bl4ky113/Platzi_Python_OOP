""" O(n) * O(n) = O(n ** 2)
"""

def sack (capacity, objs, num, status="initial", sum_money=0, items_taken=""):
    print(f"Capacity: {capacity}, iteration: {num}, status: {status}, sum_money: {sum_money}, items_taken: {items_taken}")

    # No more Items or Sack Full
    if num == 0 or capacity == 0:
        print(f"Capacity: empty or Last item")
        return 0

    if objs[num - 1][0] > capacity:
        print("Obj weights more than available")
        return sack(capacity, objs, num - 1, "weights more")

    return max(
        objs[num - 1][1] + sack(capacity - objs[num - 1][0], objs, num - 1, f"takes the item {num - 1}", sum_money + objs[num - 1][1], items_taken + f"{num - 1}"), 
        sack(capacity, objs, num - 1, f"doesnt take the item {num - 1}", sum_money, items_taken)
    )

if __name__ == "__main__":
    objs_to_steal = [
        # [weight, value]
        [10, 60],
        [20, 100],
        [30, 120]
    ]
    sack_capacity = 50
    num_items = len(objs_to_steal)

    best_item_combination = sack(sack_capacity, objs_to_steal, num_items)
    print(f"Best Result: {best_item_combination}")