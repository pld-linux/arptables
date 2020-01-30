Summary:	Arp Tables - ARP packets filtering
Summary(pl.UTF-8):	Arp Tables - filtrowanie pakietów ARP
Name:		arptables
Version:	0.0.5
Release:	1
License:	GPL v2+
Group:		Networking/Daemons
Source0:	http://ftp.netfilter.org/pub/arptables/%{name}-%{version}.tar.gz
# Source0-md5:	ca6616bedd885ac14dd1af8757fb20fa
URL:		http://ebtables.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
arptables is used to set up and maintain the tables of ARP rules in
the Linux kernel. These rules inspect the ARP frames which they see.

%description -l pl.UTF-8
arptables służy do ustawiania i zarządzania tablicami reguł ARP w
jądrze Linuksa. Reguły te dozorują ramki ARP widziane przez system.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/arptables-legacy
%attr(755,root,root) %{_sbindir}/arptables-restore
%attr(755,root,root) %{_sbindir}/arptables-save
%{_mandir}/man8/arptables-legacy.8*
%{_mandir}/man8/arptables-restore.8*
%{_mandir}/man8/arptables-save.8*
