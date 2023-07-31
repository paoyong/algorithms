const partition = function(s, l, h) {
    var i;
    var p;
    var firsthigh;
    
    p = h;
    firsthigh = l;
	for(i=l; i<h; i++)
		if (s[i] < s[p]) {
			swap(s[i], s[firsthigh])
			firsthigh++;
		}
	swap(s[p], s[firsthigh])
}

const quicksort = function(s, l, h) {
    var p;      // index of partition

    if ((h - l) > 0) {
        p = partition(s, l, h)
        quicksort(s, l, p - 1)
        quicksort(s, p + 1, h)
    }
};
