CC = gcc
CFLAGS = -Wall -Wextra -pedantic
TARGET1 = myMath
TARGET2 = myMathMain
TARGET = myMATH.c myMathMain.c

all: $(TARGET2)

$(TARGET2): $(TARGET)
	$(CC) $(CFLAGS) $(TARGET) -o $(TARGET2)

clean:
	rm $(TARGET2)
