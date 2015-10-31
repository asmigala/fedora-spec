To build the spec file:
- copy it into your rpmbuild/SPEC directory
- run:
$ spectool -g to download the source file
- copy the source file into rpmbuild/SOURCE
- run:
$ rpmbuild -ba filename.spec

The result can be found in:
- RPMS/noarch
- RPMS/x86_64

Install the rpm file using yum:
as a root user: 
$ yum install filename.rpm

To test the rebuild of the package using mock:
$ mock -r fedora-22-x86_64 --rebuild polyphone-1.6.0-1.fc22.src.rpm

ToDo:
- Add Requires in kxstudio

