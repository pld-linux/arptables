Summary:	Arp Tables
Summary(pl):	Arp Tables - filtrowanie pakietów ARP
Name:		arptables
Version:	0.0.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/%{name}/%{name}-v%{version}-2.tar.gz
# Source0-md5:	c4559af2366c764c6c42a3fdd40d60d3
Patch0:		%{name}-llh.patch
URL:		http://ebtables.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

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
