/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) { 
    // merge arrays
    for (i = m; i < m + n; i++) {
        nums1[i] = nums2[i - m]
    }

    console.log(nums1)

    // Brute Force
    for (i = m + n - 1; i > 0; i--) {
        var max_index = i
        var max = nums1[i]
        var temp;

        for (j = i - 1; j >= 0; j--) {
            if (nums1[j] > max) {
                max = nums1[j]
                max_index = j
            }
        }

        if (max_index != i) {
            temp = nums1[i]
            nums1[i] = nums1[max_index]
            nums1[max_index] = temp
        }
    }
};

var merge2 = function(arr, mid) { 
    var b1 = [];
    var b2 = [];
    var c = 0;

    for (i = 0; i < mid; i++) b1.push(arr[i])
    for (i = mid; i < arr.length; i++) b2.push(arr[i])
    console.log("b1 " + b1 + " b2 " + b2)

    while (!(b1.length == 0 || b2.length == 0)) {
        if (b1 < b2) {
            arr[c++] = b1.shift()
            console.log(i)
        } else {
            arr[c++] = b2.shift()
            console.log(i)
        }
    }

    while (b1.length != 0) arr[c++] = b1.shift()
    while (b2.length != 0) arr[c++] = b2.shift()
};

n1 = [1, 3, 4, 0, 0, 0]
n2 = [2, 5, 6]
//merge(n1, 3, n2, 3)
//console.log(n1)
n1 = [1, 3, 4, 2, 5, 6]
merge2(n1, 3)
console.log(n1)

n1 = [4, 1, 2, 3, 5, 6]
merge2(n1, 1)
console.log(n1)

n1 = [4, 5, 6, 1, 2, 3]
merge2(n1, 3)
console.log(n1)


n1 = [2, 3, 12, 20, 1, 3]
merge2(n1, 4)
console.log(n1)

n3 = [4, 5, 6, 0, 0, 0]
n4 = [1, 2, 3]
//merge(n3, 3, n4, 3)
//console.log(n3)
n5 = [4, 0, 0, 0, 0, 0]
n6 = [1, 2, 3, 5, 6]
//merge(n5, 1, n6, 5)
//console.log(n5)
