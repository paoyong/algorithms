"use strict"

const swap = function(s, a, b) {
    var temp = s[a];
    s[a] = s[b];
    s[b] = temp;
}

const partition = function(s, l, h) {
    var i;
    var p;
    var firsthigh;
    
    p = h;
    firsthigh = l;
	for(i=l; i<h; i++) { 
		if (s[i] < s[p]) {
			swap(s, i, firsthigh);
			firsthigh++;
		}
        console.log("i=" +i)
        console.log("p=" +p)
        console.log("firsthigh=" +firsthigh)
        console.log("--")
    }

    swap(s, p, firsthigh);
}

const quicksort = function(s, l, h) {
    var p;      // index of partition

    if ((h - l) > 0) {
        p = partition(s, l, h);
        quicksort(s, l, p - 1);
        quicksort(s, p + 1, h);
    }
};

var arr1 = [2, 7, 2, 3, 8, 1, 9, 0, 3, -1];
quicksort(arr1, 0, arr1.length - 1);
console.log(arr1);
