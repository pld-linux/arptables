Summary:	Arp Tables - ARP packets filtering
Summary(pl.UTF-8):	Arp Tables - filtrowanie pakietów ARP
Name:		arptables
Version:	0.0.4
Release:	1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	http://downloads.sourceforge.net/ebtables/%{name}-v%{version}.tar.gz
# Source0-md5:	c2e99c3aa9d78c9dfa30710ca3168182
URL:		http://ebtables.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arptables is used to set up and maintain the tables of ARP rules in
the Linux kernel. These rules inspect the ARP frames which they see.

%description -l pl.UTF-8
arptables służy do ustawiania i zarządzania tablicami reguł ARP w
jądrze Linuksa. Reguły te dozorują ramki ARP widziane przez system.

%prep
%setup -q -n %{name}-v%{version}

%build
%{__make} \
	CC="%{__cc}" \
	COPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}	$RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D %{name}.8	$RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/arptables
%{_mandir}/man8/arptables.8*
