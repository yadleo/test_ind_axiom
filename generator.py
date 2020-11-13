# create generators for sure lottery sets and risky lottery set

def risky_lottery(a, b):
    """
    We define a lottery as (p * e, (1 - p), p * (1 - e)) over payoffs ($10, $20, $30).
    Where ( p * e + (1 - p) + p * (1 - e) ) = 1 since
    a, and b are the size of probability sets p and e
    """
    p = [(p / a) for p in range(1, (a + 1))]
    e = [(e / b) for e in range(1, (b + 1))]
    pr_a = []
    pr_b = []
    pr_c = []
    for i in range(len(p)):
        for j in range(len(e)):
            # if ((p[i] * e[j]) + (1 - p[i]) + (1 - e[j])) == 1:
            pr_a.append((p[i] * e[j]))
            pr_b.append((1 - p[i]))
            pr_c.append(p[i] * (1 - e[j]))

    lotteries = []
    for i in range(len(pr_a)):      # check do I accidentally constraint the size of the lotteries set
        lottery = [pr_a[i], pr_b[i], pr_c[i]]
        lotteries.append(lottery)

    return lotteries


# import random
# # lottery = risky_lottery(2, 2)
# lottery = [
#     [0.25, 0.5, 0.25],
#     [0.5, 0.5, 0.0]
# ]
# print(lottery)
# results = random.sample(lottery, 1)
# print(results)
# print(risky_lottery(8, 8))

# print(len(risky_lottery(8, 8)))
# import random
# results = random.sample(risky_lottery(8, 8), 1)
# print(results)


def sure_lottery():
    """
    generate a sure lottery q = {$10, 0; $20, 1; $30, 0}
    """
    return [0, 1, 0]


# print(type(sure_lottery()))
# sure_lottery_des = "$10 with probability %s, $20 with probability %s, and $30 with probability %s" % tuple(sure_lottery())

# print(sure_lottery_des)

# test_dic = {
#     "lottery_A": "$10 with probability 0.1, $20 with probability 0.8, $30 with probability 0.1",
#     "lottery_B": "$10 with probability 0, $20 with probability 1, $30 with probability 0"
# }

# print(type(test_dic))


# participants = ["a", "b", "ccc", "dddd", "eeeee"]
# for participant in participants:
#     print(participant)
#     print(type(participant))

# lottery_pair_dic = [
#     {
#         "lotteryA": "$10 with prob 1, $20 with prob 0.5, $30 with prob 0",
#         "lotteryB": "$10 with prob 0.5, $20 with prob 0.2, $30 with prob 0.3"
#     },

#     {
#         "lotteryA": "$10 with prob 1, $20 with prob 0.5, $30 with prob 0",
#         "lotteryB": "$10 with prob 0.4, $20 with prob 0.2, $30 with prob 0.4"
#     },

#     {
#         "lotteryA": "$10 with prob 1, $20 with prob 0.5, $30 with prob 0",
#         "lotteryB": "$10 with prob 0.5, $20 with prob 0, $30 with prob 0.5"
#     },

#     {
#         "lotteryA": "$10 with prob 1, $20 with prob 0.5, $30 with prob 0",
#         "lotteryB": "$10 with prob 0.5, $20 with prob 0.4, $30 with prob 0.1"
#     },

#     {
#         "lotteryA": "$10 with prob 1, $20 with prob 0.5, $30 with prob 0",
#         "lotteryB": "$10 with prob 0.1, $20 with prob 0.6, $30 with prob 0.3"
#     },
# ]

# dic_keys = [1, 2, 3, 4, 5]
# dic_new = {}
# for key in dic_keys:
#     for item in lottery_pair_dic:
#         dic_new[key] = item
# print(dic_new)
