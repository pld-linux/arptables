Summary:	Arp Tables
Summary(pl.UTF-8):   Arp Tables - filtrowanie pakietów ARP
Name:		arptables
Version:	0.0.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/ebtables/%{name}-v%{version}-2.tar.gz
# Source0-md5:	283d19292bd99913dc3a42842826c286
Patch0:		%{name}-llh.patch
URL:		http://ebtables.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arptables is used to set up and maintain the tables of ARP rules in
the Linux kernel. These rules inspect the ARP frames which they see.

%description -l pl.UTF-8
arptables służy do ustawiania i zarządzania tablicami reguł ARP w
jądrze Linuksa. Reguły te dozorują ramki APR widziane przez system.

%prep
%setup -q -n %{name}-v%{version}-2
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name}	$RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D %{name}.8	$RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
