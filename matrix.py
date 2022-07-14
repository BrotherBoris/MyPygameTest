class Matrix():
    def __init__(this, rows, columns):
        this.rows = rows
        this.columns = columns
        this.matrix = []
        for i in range(this.rows) :
            this.matrix.append([])
            for j in range(this.columns):
                this.matrix[i].append(None)

    def fillWithThis(this, value):
        for i in range(this.rows) :
            
            for j in range(this.columns):
                this.matrix[i][j] = value

    def printGrid(this):
        for i in range(this.rows) :
            print("|", end=" ")
            for j in range(this.columns):
                print(this.matrix[i][j], end=" ")
            print("|")