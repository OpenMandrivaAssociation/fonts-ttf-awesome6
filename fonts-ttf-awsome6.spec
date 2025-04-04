#Imported from rosa

Summary:	Iconic font set awesome version 6
Name:		fonts-ttf-awesome6
Version:	6.7.2
Release:	1
License:	OFL
Group:		System/Fonts/True type
Url:		http://fontawesome.io/
Source0:	https://github.com/FortAwesome/Font-Awesome/releases/download/%{version}/fontawesome-free-%{version}-desktop.zip
Source1:	https://github.com/FortAwesome/Font-Awesome/releases/download/%{version}/fontawesome-free-%{version}-web.zip
BuildRequires:	fontpackages-devel
BuildRequires:	unzip
BuildArch:	noarch

%description
Scalable vector icons that can be customized — size, color, drop shadow,
and anything that can be done with the power of CSS.

(Note that the font does not contain regular letters)

%files
%{_datadir}/fonts/TTF/fontawesome6/*
%{_datadir}/fa-*

#--------------------------------------------------------------------------

%package web
Summary:	Web files for font awesome version 6
License:	MIT
Group:		System/Fonts/True type

%description web
Web files (css, less, scss, etc) for font awesome version 6.

%files web
%{_datadir}/fontawesome6-web/

#--------------------------------------------------------------------------

%prep
%setup -q -c
%setup -q -T -D -a1

%build

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts/TTF/fontawesome6
install -p -m 0644 */otfs/*.otf %{buildroot}%{_datadir}/fonts/TTF/fontawesome6/

install -m 0755 -d %{buildroot}%{_datadir}/fontawesome6-web/webfonts
install -p -m 0644 */webfonts/*.{ttf,woff2} %{buildroot}%{_datadir}
