/*
Name: Eric Ortiz

*/

/*
Code, compile, and execute the following code on a variety of operating systems (at the very least try a version of Linux and a version of Windows).  Comment on your observations.  Then comment on what you think the code is, what it does, how an attacker might use it, and what you might do to deal with such an attack.
*/

int main(int argc, char** argv)
{
	for (;;)
		system(argv[0]);

}

/*
The program is a fork bomb written in C. Its main purpose is to flood the computer with useless
processes. This slows the computer down to the point of restarting. Depending on the system, a hacker
could easily use this to take out a computer. This could force an admin retype their login information or
re-access a network, leaving them vulnerable to keylogger interception. At the very least, this attack
halts productivity for the user that receives the attack. To prevent the attack, the user could simply
preemptively restart their computer. Alternatively, a user could set up their computer to only allow so
many processes to be concurrent at a time. Lastly, a user could monitor their task manager to see if
command prompt or any other programs are drawing way more resources than they need.

I tested the program on Windows, Linux Mint (VM), Linux Mint (Native), and Bash Shell for Windows.
On the Bash Shell on Windows and the Linux Mint VM, the program does not slow down the computer to
the point of restarting. My guess is that there are services in place that prevent fork-bombs by restricting
the amount of resources that can be used inside these virtual environments. On Linux Mint Native,
however, once the program runs, you can no longer open any more processes. The OS springs the error
that the program failed to fork (resources are temporarily unavailable). The only time the program was
truly effective was on Windows. When the program ran on Windows, resources were continually eaten up
until nearly 100% of CPU and RAM was being consumed. Although this alone did not cause the computer
to shut down automatically, it did cause the CPU to run extremely hot, forcing me to manually shut
the computer down.

It is also worth mentioning that after the command prompt or terminal has been closed, all instances of the
program seem to die, returning the computer back to a usable state.
*/