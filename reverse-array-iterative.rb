def reverse_array(a)
    right = a.length-1
    left = 0
    
    while(left < right)
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        
        left + 1
        right -= 1
    end
    print a
end

reverse_array([12,1313,555,6])