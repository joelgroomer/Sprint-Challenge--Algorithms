#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n)
This code is going to loop `n` times no matter what. You can think of it as `n^3 / n^2 = n` because the rate at which `a` increases is `n^2` towards the final value specified in the while loop, `n * n * n`.

for n = 3, n^3 = 27
1: 9
2: 18
3: 27

for n = 300, n^3 = 27,000,000
1: 90,000
2: 180,000
3: 270,000
100: 9,000,000
300: 27,000,000

b) O(n^2)
The outer loop will run `n` times. The inner loop will run `n / 2` times. The result is `n * n/2` or `n^2 / 2` which reduces to `n^2` when ignoring the constant.

c) O(n)
This function will call itself recursively, but only once per `n`. It's basically the same as a for loop.

## Exercise II

I would use a binary search for this, starting at the middle floor. If the egg survives, move up half of the floors remaining and test again. If it doesn't survive, move down half of the floors remaining instead.

```python
def egg_test(floors):
    low = 1
    high = floors
    highest_unbroken = None
    while high - low > 1:
        floor = low + ((high - low) // 2)
        broken = drop_egg_from(floor)
        if broken:
            high = floor
        else:
            low = floor
            highest_unbroken = floor
    return highest_unbroken
```
