#include "exceptions.h"

//UIException
UIException::UIException(const std::string& message) : m_message(message) {}
const char* UIException::what() const noexcept {
    return m_message.c_str();
}

//ServException
ServException::ServException(const std::string& message) : m_message(message) {}
const char* ServException::what() const noexcept {
    return m_message.c_str();
}

//RepoException
RepoException::RepoException(const std::string& message) : m_message(message) {}
const char* RepoException::what() const noexcept {
    return m_message.c_str();
}
