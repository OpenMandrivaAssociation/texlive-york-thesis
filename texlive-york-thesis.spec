# revision 23348
# category Package
# catalog-ctan /macros/latex/contrib/york-thesis
# catalog-date 2011-06-14 00:09:45 +0200
# catalog-license lppl1.3
# catalog-version 3.6
Name:		texlive-york-thesis
Version:	3.6
Release:	3
Summary:	A thesis class file for York University, Toronto
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/york-thesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/york-thesis.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
York Graduate Studies has again changed the requirements for
theses and dissertations. The established york-thesis class
file now implements the changes made in Spring 2005.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/york-thesis/york-thesis.cls
%doc %{_texmfdistdir}/doc/latex/york-thesis/README
%doc %{_texmfdistdir}/doc/latex/york-thesis/york-thesis-Template.tex
%doc %{_texmfdistdir}/doc/latex/york-thesis/york-thesis.el
%doc %{_texmfdistdir}/doc/latex/york-thesis/york-thesis.pdf
#- source
%doc %{_texmfdistdir}/source/latex/york-thesis/york-thesis.dtx
%doc %{_texmfdistdir}/source/latex/york-thesis/york-thesis.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.6-2
+ Revision: 757745
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.6-1
+ Revision: 719966
- texlive-york-thesis
- texlive-york-thesis
- texlive-york-thesis

