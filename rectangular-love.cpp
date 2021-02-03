  class RangeOverlap
{
private:
    int startPoint_;
    int length_;

public:
    RangeOverlap() :
        startPoint_(0),
        length_(0)
    {
    }

    RangeOverlap(int startPoint, int width) :
        startPoint_(startPoint),
        length_(width)
    {
    }

    int getStartPoint() const
    {
        return startPoint_;
    }

    int getLength() const
    {
        return length_;
    }

    bool overlapExists() const
    {
        return length_ > 0;
    }

    bool operator==(const RangeOverlap& other) const
    {
        return
            startPoint_ == other.startPoint_
            && length_ == other.length_;
    }

    bool operator!=(const RangeOverlap& other) const
    {
        return !(*this == other);
    }
};


RangeOverlap findRangeOverlap(int point1, int length1, int point2, int length2)
{

    // find the highest start point and lowest end point.
    // the highest ("rightmost" or "upmost") start point is
    // the start point of the overlap.
    // the lowest end point is the end point of the overlap.
    int highestStartPoint = max(point1, point2);
    int lowestEndPoint = min(point1 + length1, point2 + length2);

    // return null overlap if there is no overlap
    if (highestStartPoint >= lowestEndPoint) {
        return RangeOverlap();
    }

    // compute the overlap length
    int overlapLength = lowestEndPoint - highestStartPoint;

    return RangeOverlap(highestStartPoint, overlapLength);
}