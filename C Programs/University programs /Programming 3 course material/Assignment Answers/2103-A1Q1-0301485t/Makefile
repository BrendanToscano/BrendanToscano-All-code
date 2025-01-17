CC = gcc
CFLAGS = -Wall -Wextra -pedantic
TARGET1 = add
TARGET2 = loop

all: $(TARGET1) $(TARGET2)

$(TARGET1): $(TARGET1).c
	$(CC) $(CFLAGS) -o $(TARGET1) $(TARGET1).c

$(TARGET2): $(TARGET2).o
	$(CC) $(CFLAGS) -o $(TARGET2) $(TARGET2).o

$(TARGET2).o: $(TARGET2).c
	$(CC) $(CFLAGS) -c $(TARGET2).c

clean:
	rm $(TARGET1) $(TARGET2) *.o


