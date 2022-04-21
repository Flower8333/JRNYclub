import random
def key_mint(key_num, rolls_num):
    dudes_inside_keys = ["Ape", "Rabid", "Xolian", "1 of 1", "Villager"]
    probabilities = [1.54, 1.2, 0.43, 0.06, 96.77]
    results = []
    n = 0
    while n != rolls_num:
        n += 1
        count_of_dudes_in_each_set = {}
        for specific_mint in range(key_num):
            x = random.choices(dudes_inside_keys, weights=probabilities)
            species = x[0]
            if species not in count_of_dudes_in_each_set:
                count_of_dudes_in_each_set[species] = int()
            count_of_dudes_in_each_set[species] += 1
        results.append(count_of_dudes_in_each_set)

    print(results)
    rares_minted = 0
    for specific_roll in results:
        if len(specific_roll) != 1:
            rares_minted += 1

    probability_of_minting_rare = 100 * rares_minted / rolls_num
    return "Probability of getting a rare on", key_num," rolls is:", probability_of_minting_rare

print(key_mint(7, 1000))








