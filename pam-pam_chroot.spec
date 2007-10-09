%define 	modulename pam_chroot
Summary:	PAM chroot module
Summary(pl.UTF-8):	Moduł PAM zamykający użytkownika w chroocie
Name:		pam-%{modulename}
Version:	0.9.1
Release:	0.1
Epoch:		0
License:	GPL v2
Vendor:		Ed Schmollinger <schmolli@frozencrow.org>
Group:		Applications/System
Source0:	http://dl.sourceforge.net/pam-chroot/pam_chroot-%{version}.tar.gz
# Source0-md5:	444033be96a999d801dd49e06268b0d6
URL:		http://sourceforge.net/projects/pam-chroot/
BuildRequires:	pam-devel
Obsoletes:	pam_chroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which allows to chroot user environment.

%description -l pl.UTF-8
Moduł PAM pozwalający na zamknięcie użytkownika w chroocie.

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-fPIC %{rpmcflags} -Wall -Werror -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/security,/%{_lib}/security}

install pam_chroot.so $RPM_BUILD_ROOT/%{_lib}/security
install chroot.conf $RPM_BUILD_ROOT/etc/security/chroot.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS options
%attr(755,root,root) /%{_lib}/security/pam_chroot.so
%config(noreplace) %verify(not md5 mtime size) /etc/security/chroot.conf
