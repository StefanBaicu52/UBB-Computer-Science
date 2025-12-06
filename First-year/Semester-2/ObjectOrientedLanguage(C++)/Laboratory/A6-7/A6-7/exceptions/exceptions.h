#ifndef EXCEPTIONS_H
#define EXCEPTIONS_H

#pragma once
#include <string>
#include <exception>

class UIException :
public std::exception {
    private:
        std::string m_message;
    public:
        explicit UIException(const std::string& message);
        const char* what() const noexcept override;
};


class ServException :

public std::exception {

    private:
        std::string m_message;
    public:
        explicit ServException(const std::string& message);
        const char* what() const noexcept override;
};

class RepoException :

public std::exception {
    private:
        std::string m_message;
    public:
        explicit RepoException(const std::string& message);
        const char* what() const noexcept override;
};


#endif