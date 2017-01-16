/***************************************
 *
 * Convert hexadecimal string to Base64
 *
 ***************************************/

#include <openssl/bio.h>
#include <openssl/evp.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "dbg.h"

const unsigned char basis16[16] = "0123456789ABCDEF";

int scan_basis16(char c) {
	c = toupper(c);
	for(int i = 0; i <= 16; i++) {
		if (c == basis16[i]) {
			// debug("c = '%c' maps to %d", c, i);
			return i;
		}
	}
	sentinel("character '%c' not part of base 16", c);
error:
	return -1;
}

unsigned char *hexstr2buf(char *str, int *len) {
	check( (*len == strlen(str)), "*len must be the strlen *str. *len = %ul, strlen = %lu", *len, strlen(str));
	check( (*len % 2 == 0), "There must be an even number of hex chars");
	check( (str[*len] == '\0'), "*str must terminate in a null byte.");

	unsigned char *result;
	int ln, rn; // upper (left) and lower (right) nibbles of hex byte
	int buflen = (*len) / 2; // two hex chars per byte
	debug("buflen = %i", buflen);
	result = malloc(buflen);
	check_mem(result);
	memset(result, '\0', buflen);

	for(int i = 0; i < buflen; i++) {
		ln = scan_basis16(str[2*i]);
		rn = scan_basis16(str[2*i + 1]);
		check( (ln != -1) && (rn != -1), "Invalid character in hex string");
		result[i] = (ln << 4) | rn;
	}

	*len = buflen;
	debug("result = %s", result);
	return result;

error:
	return NULL;
}

int main(int argc, char *argv[]) {
	BIO *bio, *b64 = NULL;
	char str[] = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	int *len = malloc(sizeof(int));
	char *p_str = str;
	unsigned char *hexbuf = NULL;

	*len = strlen(str);
	debug("*len = %d", *len);
	hexbuf = hexstr2buf(p_str, len);

	b64 = BIO_new(BIO_f_base64());
	bio = BIO_new_fp(stdout, BIO_NOCLOSE);
	BIO_push(b64, bio);
	BIO_set_flags(bio, BIO_FLAGS_BASE64_NO_NL); //Do not use newlines to flush buffer
	BIO_write(b64, hexbuf, *len);
	BIO_flush(b64);

	BIO_free_all(b64);
	free(hexbuf);
	return 0;
}