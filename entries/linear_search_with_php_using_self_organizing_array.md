----
category: PHP
create_date: 2011-12-20
description: In this entry I'll show how a linear search on an array can be efficient, given that we're repeatidly trying to find the same set of values.
title: Efficient linear search w\ PHP on a sorted array
keywords: linear search php, linear search, find php array, linear search array, linear search php array
slug: linear-search-with-php-using-self-organizing-array
----

Given the right circumstances a linear search can be an effective and
efficient way of finding a value on a sorted list.

One of such occasions would be when you are trying to find a value (or a set
of values) repeatedly. If you know that only a small subset of your list is
frequently searched for, a solution would&nbsp_place_holder; be to make sure
that the values that are commonly searched are kept on top of the list - this
way you'll know that on the vast majority of times the number of iterations
required to find one of those values will be low.

You may take a couple of approaches:

  1. Every time you find an item, move it to the top of the list.
  2. Every time you find an item, move it up by one position.

The approach you should take depends on what you are trying to achieve (and
the set of data you're working with).

For this demonstration, I'll use the second approach. The small **PHP**
snippet bellow shows a sample implementation of the algorithm:

    
    <?php
    function linear_search(&$haystack, $needle)
    {
    	// Append a sentinel to the end of the array
    	$haystack[] = $needle;
    	$i = 0;
    	
    	while($haystack[$i++] != $needle);
    
    	// Found something
    	if($i < count($haystack)) {
    		
    		// Put the needle on top of the stack and remove it from its previous position
    		array_splice($haystack, $i - 2, 0, $haystack[$i - 1]);
    		unset($haystack[$i], $haystack[count($haystack)]);
    		return $i;
    	}
    	
    	return false;
    }
    
    $temp = array( 2, 2, 3, 4, 5, 14, 23, 23.5, 44, 52, 72 );
    $find = 23.5;
    
    echo ($it = linear_search($temp, $find)) ? "Yup, {$find} is here, took me {$it} iterations...<br />" : "Nope, not there.<br />";
    echo ($it = linear_search($temp, $find)) ? "Yup, {$find} is here, took me {$it} iterations...<br />" : "Nope, not there.<br />";
    echo ($it = linear_search($temp, $find)) ? "Yup, {$find} is here, took me {$it} iterations...<br />" : "Nope, not there.<br />";

The expected output is something like this:

    
    Yup, 23.5 is here, took me 8 iterations...
    Yup, 23.5 is here, took me 7 iterations...
    Yup, 23.5 is here, took me 6 iterations...

As you can easily figure out as the number of searches increase, the order of
the list would start to change so that the most commonly search values would
be placed on top.

I'll try to follow up this entry with a couple of other search algorithms next
week - namelly the **Jump Search** and the **Binary Search ******algorithms.

