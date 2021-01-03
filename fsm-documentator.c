enum state {
	Init,
	Parse,
	Compute,
	Save,
	Stop
};
int main(void) {
	enum state state = Init;
	do {
		switch(state) {
		case Init://@DOT: Init->Parse
			state = Parse;
		case Parse://@DOT: Parse->Compute
			state = Compute;
		case Compute: //@DOT: Compute->Save
			state = Save;
		case Save: //@DOT: should fail
			state = Stop;
		case Stop: // @DOT: Stop->Stop
			state = Stop;
		default:
			state = Stop;
		}
	} while (state != Stop);
	return 0;
}
