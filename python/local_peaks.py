def pick_peaks(numbers):
    results = {'pos': [], 'peaks': []}
    rising = False
    if len(numbers) > 0:
        local_max = [0, numbers[0]]
        for i in range(1, len(numbers)):
            if local_max[1] < numbers[i]:
                local_max = [i, numbers[i]]
                rising = True
            elif local_max[1] > numbers[i]:
                if rising:
                    results['pos'].append(local_max[0])
                    results['peaks'].append(local_max[1])
                    rising = False
                local_max = [i, numbers[i]]
    return results


my_arr = []
print(pick_peaks(my_arr))
