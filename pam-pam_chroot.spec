%define 	modulename pam_chroot
Summary:	PAM chroot module
Summary(pl):	Modu³ PAM zamykaj±cy u¿ytkownika w chroocie
Name:		pam-%{modulename}
Version:	0.6
Release:	1
Epoch:		0
License:	GPL v2
Vendor:		Ed Schmollinger <schmolli@frozencrow.org>
Group:		Applications/System
Source0:	http://www.kernel.org/pub/linux/libs/pam/pre/modules/pam_chroot-%{version}.tar.bz2
# Source0-md5:	cd8ee12235c6bee6b825c295443bd8ae
URL:		http://www.kernel.org/pub/linux/libs/pam/pre/modules/
BuildRequires:	pam-devel
Obsoletes:	pam_chroot
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PAM module which allows to chroot user enviroment.

%description -l pl
Modu³ PAM pozwalaj±cy na zamkniêcie u¿ytkownika w chroocie.

%prep
%setup -q -n %{modulename}-%{version}

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="-fPIC %{rpmcflags} -Wall -Werror -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/security,lib/security}

install pam_chroot.so $RPM_BUILD_ROOT/lib/security
install chroot.conf $RPM_BUILD_ROOT%{_sysconfdir}/security/chroot.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS options
%attr(755,root,root) /lib/security/pam_chroot.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/security/chroot.conf
