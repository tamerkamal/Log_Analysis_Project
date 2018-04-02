# Python 2.7.12

import psycopg2


def get_TopArticles():

    db = psycopg2.connect(
        "dbname='news' user='postgres' host='localhost' password='password'")
    c = db.cursor()
    c.execute(
        """SELECT title, COUNT (path) FROM log inner join articles on SUBSTRING (path ,10) = slug   -- # noqa    
        where path like '%article%'
        GROUP BY title
        order by count (path) desc limit 3""")

    TopArticles = c.fetchall()

    Line = " ---------------------------------------------"

    print Line
    print " The most popular three articles of all time :"
    print Line
    for row in TopArticles:
        print "  * ", row[0], "__", row[1], " Views"
    print Line
    db.close()
    return TopArticles


def get_TopAuthorArticles():

    db = psycopg2.connect(
        "dbname='news' user='postgres' host='localhost' password='password'")
    c = db.cursor()
    c.execute(
        """
        SELECT Au.name,count(Lo.path)
        from articles Ar
        inner join authors Au on Ar.author = Au.id
        inner join log Lo on SUBSTRING (path ,10) =Ar.slug
        group by (Au.name)
        order by count(Lo.path) desc

        """)

    TopAuthors = c.fetchall()
    Line = " ---------------------------------------------"
    print " The Authors Popularity:"
    print Line
    for row in TopAuthors:
        print "  * ", row[0], "__", row[1], " Views"
    print Line
    db.close()
    return TopAuthors


def get_Percentage():

    db = psycopg2.connect(
        "dbname='news' user='postgres' host='localhost' password='password'")
    c = db.cursor()

    c.execute(
        """
     
    SELECT AllStatusView.V1Day, ((FailedStatusView.CountDayFailedStatus ::double precision /  -- # noqa
                                  AllStatusView.CountAllDayStatus ::double precision) * 100)
    as Percent
    From AllStatusView 
    inner join FailedStatusView 
    on V1Day = V2Day
    where ((FailedStatusView.CountDayFailedStatus ::double precision /
            AllStatusView.CountAllDayStatus ::double precision) * 100)>1;

        """)

    TopAuthors = c.fetchall()
    Line = " ---------------------------------------------"
    print " The Days where Error-Status > 1%:"
    print Line
    for row in TopAuthors:
        print " ", row[0].strftime('%B %d, %Y'), "__", round(row[1], 1), "%", " errors"    # noqa
    print Line
    db.close()
    return TopAuthors


def main():
    get_TopArticles()
    get_TopAuthorArticles()
    get_Percentage()

if __name__ == "__main__":
    main()
