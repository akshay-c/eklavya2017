1.Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition.
So if our object has a white color out of a black background , contour covers all points of the image, So before finding contours, apply threshold or canny edge detection.In Open CV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

2.Whenever we are defining a class in python we should keep in mind-
The rule of thumb is, don't introduce a new attribute outside of the __init__ method, otherwise you've given the caller an object that isn't fully initialized. There are exceptions, of course, but it's a good principle to keep in mind. This is part of a larger concept of object consistency: there shouldn't be any series of method calls that can result in the object entering a state that doesn't make sense.
[ Src : [https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/](https://jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)

3.Whereas slicings on lists and tuples create new objects, a slicing operation on an array creates a view on the original array. So we get an another possibility to access the array, or better a part of the array. From this follows that if we modify a view, the original array will be modified as well.
[ Src: [http://www.python-course.eu/numpy.php](http://www.python-course.eu/numpy.php) ]
