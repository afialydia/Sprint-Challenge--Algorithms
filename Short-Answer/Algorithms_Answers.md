#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear time because the while loop runs an n number of times? o(n)?


b) We're looping here. 'n' has to be calculated twice so that slows things down? would this be linerithmic O(n log n)?


c) Linear time? O(n) because it's only running once per bunny in the param??


## Exercise II

Binary Search would be most benetifial for this problem. Binary search requires an ordered array and searching can happen randomly rather than from left to right or top to bottom. For this problem it works because buildings generally have all floors are labeled accordingly. I would divide the floors in half by the length of the array, or in the terms of this problem by the amount of total floors available. and drop an egg from that floor. if it breaks, i would run the function again but have the range be from the lowest floor to one less than the floor i just tested. and repeat the splitting accordingly until I've found a range and or floor where the result is different.I'd also set a case for if it does not break on the initial drop. if that is the case than i would run the function again but only with the range of one past the floor i tested to the end of the array. In the end I'd return last floor that eggs can safely be dropped without being broken. 

Binary Search is 0(log n)