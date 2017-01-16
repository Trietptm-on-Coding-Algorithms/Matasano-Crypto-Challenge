CC = cc
SSL_LINKLD = -L/usr/lib
SSL_INCLUDES = -I/usr/include/openssl
CFLAGS = -Wall -Wno-deprecated-declarations -g -lcrypto
#CFLAGS += -D_DEBUG

hex64: hex64.c
	$(CC) -o hex64 hex64.c $(CFLAGS)

clean:
	$(RM) hex64
	$(RM) -r "*.dSYM"